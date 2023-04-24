#include <stdio.h>


// Endianness herausfinden
// Ich benutze den Byte von 1
// Falls dieser Bite ausgleicht ist dein System (CPU) little Endian
// Falls sich dieser Bite nicht eins gleicht (also ist es falschrum) verwendet dein System Big Endian
// Das Ganze mache ich mit einfach if statements (fast wie in Python)
// Macht in Programiz mit
int main()
{
	int i = 1;

	if (*((char*)&i) == 1) puts("Dein System verwendet little Endian!");
	else puts("Dein System verwendet Big Endian");


	return 0;
}
