----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 04/12/2021 03:56:42 PM
-- Design Name: 
-- Module Name: Data_Memory - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


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
