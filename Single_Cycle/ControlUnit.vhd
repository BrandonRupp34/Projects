

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
