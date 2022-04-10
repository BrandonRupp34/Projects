
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
