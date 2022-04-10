
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
