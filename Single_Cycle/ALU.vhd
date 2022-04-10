
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
