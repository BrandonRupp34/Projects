
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity SingleCycleMips is
    Port ( PC : in STD_LOGIC_VECTOR (31 downto 0);
           Clk: in STD_LOGIC);
           --Result: out STD_LOGIC_VECTOR (31 downto 0));
        
end SingleCycleMips;

architecture Behavioral of SingleCycleMips is

    component Instruction_memory is
        Port ( PC : in STD_LOGIC_VECTOR (31 downto 0);
               Instr : out STD_LOGIC_VECTOR (31 downto 0));
    end component;
    
    component Register_File is
        Port ( A1, A2, A3 : in STD_LOGIC_VECTOR (4 downto 0);
               Input : in STD_LOGIC_VECTOR (15 downto 0);
               Clk, WE3, RegDst : in STD_LOGIC;
               WD3 : in STD_LOGIC_VECTOR (31 downto 0);
               RD1, RD2, SignImm : out STD_LOGIC_VECTOR (31 downto 0));
        
    end component;
           
    component ControlUnit is
        Port ( Funct : in STD_LOGIC_VECTOR (5 downto 0);
               Opcode : in STD_LOGIC_VECTOR (5 downto 0);
               ALUControl : out STD_LOGIC_VECTOR (2 downto 0);
               MemtoReg, MemWrite, Branch, ALUSrc, RegDst, RegWrite : out STD_LOGIC); 
               
    end component;
    
    component ALU is
    Port ( A, B : in STD_LOGIC_VECTOR (31 downto 0);
           ALUControl : in STD_LOGIC_VECTOR (2 downto 0);
           Result : out STD_LOGIC_VECTOR (31 downto 0));
    end component;
          
    component Data_Memory is
    Port ( A, WD : in STD_LOGIC_VECTOR (31 downto 0);
           Clk, WE : in STD_LOGIC;
           RD : out STD_LOGIC_VECTOR (31 downto 0));
    end component;
    
    component Result_MUX is
    port ( Result, RD: in STD_LOGIC_VECTOR (31 downto 0);
           MemToReg: in STD_LOGIC;
           Output: out STD_LOGIC_VECTOR (31 downto 0));
    end component;
    
    component SignImm_MUX is
    Port (RD2, SignImm: in STD_LOGIC_VECTOR(31 downto 0);
          ALUSrc: in STD_LOGIC;
          SrcB: out STD_LOGIC_VECTOR(31 downto 0));
    end component;



    Signal Instr, Output : STD_LOGIC_VECTOR (31 downto 0);
    Signal WD3, RD1, RD2 : STD_LOGIC_VECTOR (31 downto 0);
    Signal RD : STD_LOGIC_VECTOR (31 downto 0); 
    Signal Input : STD_LOGIC_VECTOR(15 downto 0);
    Signal SignImm : STD_LOGIC_VECTOR(31 downto 0);
    Signal WE, MemtoReg, MemWrite, Branch, ALUSrc, RegDst, RegWrite : STD_LOGIC;
    Signal SrcA, SrcB : STD_LOGIC_VECTOR (31 downto 0);
    Signal ALUControl : STD_LOGIC_VECTOR (2 downto 0);
    Signal Result : STD_LOGIC_VECTOR (31 downto 0);
    Signal Opcode : STD_LOGIC_VECTOR (5 downto 0);
    Signal ALUOp : STD_LOGIC_VECTOR (1 downto 0);
    Signal Funct : STD_LOGIC_VECTOR (5 downto 0);

begin


IM: Instruction_Memory port map (PC(31 downto 0), Instr(31 downto 0));

CU: ControlUnit port map(Instr(5 downto 0), Instr(31 downto 26), ALUControl, MemtoReg, MemWrite, Branch, ALUSrc, RegDst, RegWrite);

RG: Register_File port map(Instr(25 downto 21), Instr(20 downto 16), Instr(15 downto 11), Instr(15 downto 0), Clk, RegWrite, RegDst, Output, RD1, RD2, SignImm);

AU: ALU port map(RD1, SrcB, ALUControl, Result);

DM: Data_Memory port map(Result, RD2, Clk, MemWrite, RD);

RM: Result_MUX port map(Result, RD, MemToReg, Output);

SM: SignIMM_MUX port map(RD2, SignIMM, ALUSrc, SrcB);

end Behavioral;
























library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;


entity Instruction_memory is
    Port ( PC : in STD_LOGIC_VECTOR (31 downto 0);
           Instr : out STD_LOGIC_VECTOR (31 downto 0));
end Instruction_memory;

architecture Behavioral of Instruction_memory is

type instruction_memory is array (5 downto 0) of std_logic_vector(31 downto 0);
signal vals : instruction_memory := (
-- 
x"02328020", -- add $s0, $s1, $s2 
x"8C0A0020", -- lw $t2, 32($0) 
x"AD310004", -- sw $s1, 4($t1)
x"2237FFF1", -- addi $s7, $s1, -15
x"112B000C", -- BEQ $r9, $r11, 12
x"08000008" -- Jump 8
);


begin

Instr <= vals(to_integer(unsigned(PC)));


end Behavioral;




















library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ControlUnit is
    Port ( --Instr : in STD_LOGIC_VECTOR (31 downto 0);
           Funct : in STD_LOGIC_VECTOR (5 downto 0);
           Opcode : in STD_LOGIC_VECTOR (5 downto 0);
           ALUControl : out STD_LOGIC_VECTOR (2 downto 0);
           MemtoReg, MemWrite, Branch, ALUSrc, RegDst, RegWrite : out STD_LOGIC); 
           
end ControlUnit;

architecture Behavioral of ControlUnit is

component MainDecoder is
    Port ( Opcode : in STD_LOGIC_VECTOR (5 downto 0);
           MemtoReg, MemWrite, Branch, ALUSrc, RegDst, RegWrite : out STD_LOGIC;  
           ALUOp : out STD_LOGIC_VECTOR (1 downto 0));
end component;            

component ALUDecoder is 
    Port ( Funct : in STD_LOGIC_VECTOR (5 downto 0);
           ALUOp : in STD_LOGIC_VECTOR (1 downto 0);
           ALUControl : out STD_LOGIC_VECTOR (2 downto 0));
end component;

Signal ALUOp : STD_LOGIC_VECTOR (1 downto 0);
--Signal OpCode : STD_LOGIC_VECTOR (5 downto 0);
--Signal Funct : STD_LOGIC_VECTOR (5 downto 0);

begin
--OpCode <= Instr(31 downto 26);
--Funct <= Instr(5 downto 0);

Process (OPCode)

    begin

if OPCode = "000000" then 
    MemtoReg <= '0'; MemWrite <= '0'; Branch <= '0'; ALUSrc <= '0'; RegDst <= '1'; RegWrite <= '1'; ALUOp(1) <= '1'; ALUOp(0) <= '0';
elsif OPCode = "100011" then
    MemtoReg <= '1'; MemWrite <= '0'; Branch <= '0'; ALUSrc <= '1'; RegDst <= '0'; RegWrite <= '1'; ALUOp(1) <= '0'; ALUOp(0) <= '0';
elsif OPCode = "101011" then
    MemtoReg <= '-'; MemWrite <= '1'; Branch <= '0'; ALUSrc <= '1'; RegDst <= '-'; RegWrite <= '0'; ALUOp(1) <= '0'; ALUOp(0) <= '0';
elsif OPCode = "000100" then
    MemtoReg <= '-'; MemWrite <= '0'; Branch <= '1'; ALUSrc <= '0'; RegDst <= '-'; RegWrite <= '0'; ALUOp(1) <= '0'; ALUOp(0) <= '1';
elsif OPCode = "001000" then
    MemtoReg <= '0'; MemWrite <= '0'; Branch <= '0'; ALUSrc <= '1'; RegDst <= '0'; RegWrite <= '1'; ALUOp(1) <= '0'; ALUOp(0) <= '0';
elsif OPCode = "000010" then
    MemtoReg <= '-'; MemWrite <= '0'; Branch <= '-'; ALUSrc <= '-'; RegDst <= '-'; RegWrite <= '0'; ALUOp <= "--";       
else
    NULL;
    
end if;

end process;

Process(ALUOp, Funct)
    
    begin

if (ALUOp = "00") then
    ALUControl <= "010";
elsif (ALUOp(0) = '1') then
    ALUControl <= "110";
elsif (ALUOp(1) = '1') then
    if Funct = "100000" then 
        ALUControl <= "010";
    elsif Funct = "100010" then
        ALUControl <= "110";
    elsif Funct = "100100" then 
        ALUControl <= "000";
    elsif Funct = "100101" then
        ALUControl <= "001";
    elsif Funct = "101010" then
        ALUControl <= "111";
    else 
        NULL;
    end if;
   -- ALUControl(0) <= ((Funct(5) and Funct(4)) and ((not(Funct(3)) and Funct(2) and not(Funct(1)) and Funct(0)) or ((not(Funct(2)) and Funct(3) and not(Funct(0)) and Funct(1)))));
   -- ALUControl(1) <= (Funct(5) and not(Funct(4)) and not(Funct(2)) and not(Funct(0)) and (not(Funct(3)) or (Funct(3) and Funct(1))));
    --ALUControl(2) <= (Funct(5) and not(Funct(4)) and not(Funct(2)) and Funct(1) and not(Funct(0)));
else 
    NULL;
end if;

end process;

end Behavioral;


















library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Register_File is
    Port ( A1, A2, A3 : in STD_LOGIC_VECTOR (4 downto 0);
           Input : in STD_LOGIC_VECTOR (15 downto 0);
           Clk, WE3, RegDst : in STD_LOGIC;
           WD3 : in STD_LOGIC_VECTOR (31 downto 0);
           RD1, RD2, SignImm : out STD_LOGIC_VECTOR (31 downto 0));
           
           
end Register_File;

architecture Behavioral of Register_File is 


type reg_file is array (31 downto 0) of std_logic_vector(31 downto 0);

signal registers : reg_file := (
-- ACSII Default values for all registers
x"00000097", x"00000098", x"00000099", x"00000100", x"00000101", x"00000102", x"00000103", x"00000104",  
x"00000105", x"00000106", x"00000107", x"00000108", x"00000109", x"00000110", x"00000111", x"00000112",
x"00000113", x"00000114", x"00000115", x"00000116", x"00000117", x"00000118", x"00000119", x"00000120",
x"00000121", x"00000122", x"00000123", x"00000124", x"00000125", x"00000126", x"00000127", x"00000128"
);

Signal A4 : STD_LOGIC_VECTOR (4 downto 0); 

begin

Process(clk)
begin
if rising_edge(clk) then
    
    if (WE3 = '1') then
        
        case (RegDst) is
            when '0' => A4 <= A2;    -- multiplexer
            when '1' => A4 <= A3;
            when others => NULL;
            end case;
            
            registers(to_integer(unsigned(A4))) <= WD3;
    
    else 
         
         RD1 <= registers(to_integer(unsigned(A1)));
         RD2 <= registers(to_integer(unsigned(A2)));
         
    end if;
    
else 
    NULL;

end if;
end process;

Sign_Extend: process(Input)
begin

if (Input(15) = '1') then
    SignImm(31 downto 16) <= x"FFFF";
    
elsif (Input(15) = '0') then
     SignImm(31 downto 16) <= x"0000";
    
else 
    NULL;

end if;


end process;
end Behavioral;















library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.std_logic_unsigned.all;

entity ALU is
    Port ( A, B : in STD_LOGIC_VECTOR (31 downto 0);
           ALUControl : in STD_LOGIC_VECTOR (2 downto 0);
           Result : out STD_LOGIC_VECTOR (31 downto 0));
end ALU;

architecture Behavioral of ALU is

begin
process(A,B,ALUControl)
begin

Case ALUControl is
    when "010" => Result <= A + B;
    when "110" => Result <= A - B;
    when "011" => Result <= not(A);
    when "100" => Result <= A xor B;
    when "000" => Result <= A and B;
    when "001" => Result <= A or B;
    when "111" =>
        if (A < B) then
            Result <= x"00000001";
        elsif (A > B) then
            Result <= x"00000000";
        else
            NULL;
        end if;
    when others =>
        NULL;
end case;
end process;

end Behavioral;
























library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;


entity Data_Memory is
    Port ( A, WD : in STD_LOGIC_VECTOR (31 downto 0);
           Clk, WE : in STD_LOGIC;
           RD : out STD_LOGIC_VECTOR (31 downto 0));
end Data_Memory;

architecture Behavioral of Data_Memory is

type data_memory is array (31 downto 0) of std_logic_vector(31 downto 0);
signal vals : data_memory := (
-- 
x"00000000", x"00000001", x"00000002", x"00000003", x"00000004", x"00000005",
x"00000006", x"00000007", x"00000008", x"00000009", x"00000010", x"00000011",
x"00000012", x"00000013", x"00000014", x"00000015", x"00000016", x"00000017",
x"00000018", x"00000019", x"00000020", x"00000021", x"00000022", x"00000023",
x"00000024", x"00000025", x"00000026", x"00000027", x"00000028", x"00000029",
x"00000030", x"00000031"
);

begin
process(Clk, WE)
begin

    if (WE = '1') then
        if (rising_edge(clk)) then
            vals(to_integer(unsigned(A))) <= WD;
        else
            NULL;
        end if;
    elsif (WE = '0') then
        RD <=  vals(to_integer(unsigned(A)));
    else 
        NULL;
                   
end if;
end process;
end Behavioral;






















library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Result_MUX is
    port ( Result, RD: in STD_LOGIC_VECTOR (31 downto 0);
           MemToReg: in STD_LOGIC;
           Output: out STD_LOGIC_VECTOR (31 downto 0));
end Result_MUX;

architecture Behavioral of Result_MUX is

begin
process
begin

if(MemToReg = '0') then
    Output <= Result;
elsif (MemToReg = '1') then
    Output <= RD;

end if;
end process;
end Behavioral;
















library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity SignImm_MUX is
    Port (RD2, SignImm: in STD_LOGIC_VECTOR(31 downto 0);
          ALUSrc: in STD_LOGIC;
          SrcB: out STD_LOGIC_VECTOR(31 downto 0));
end SignImm_MUX;

architecture Behavioral of SignImm_MUX is

begin
process
begin

if (ALUSrc = '0') then
    SrcB <= RD2;
elsif (ALUSrc = '1') then
    SrcB <= SignImm;
end if;

end process;
end Behavioral;
