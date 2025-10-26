/***********************************************************************
 *   ____   ___    _
 *  / ___| |_ _|  / \
 *  \___ \  | |  / _ \
 *   ___) | | | / ___ \
 *  |____/ |___/_/   \_\
 *
 *  File:        <filename>.c
 *  Author:      SIA
 *  Description: <brief description of the file>
 *  Created:     <date>
 **********************************************************************/

#include <stdio.h>
#include <stdint.h>


//----------------------------------------------------------------------
class PrintDebug
{
  public:
    static void print_mem_bytes(void* ptr, size_t byte_count)
    {
        uint8_t* byte_ptr = static_cast<uint8_t*>(ptr);
        // print address table header
        printf(
            "\n Address         +0  +1  +2  +3"
            "\n ------------------------------"
        );

        // loop through bytes and print values stored in memory
        for(int i = 0; i<byte_count; i++)
        {
            // print address every 4 bytes
            if(reinterpret_cast<uint64_t>(byte_ptr)%4 == 0)
            {
                printf("\n %p  ",byte_ptr);
            }

            // print byte in memory
            printf("%2X  ", *(byte_ptr++));
        }
        printf("\n\n");
        return;
    }
};
