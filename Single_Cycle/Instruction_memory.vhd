
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
