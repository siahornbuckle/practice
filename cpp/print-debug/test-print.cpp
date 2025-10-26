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

#include <stdint.h>
#include "print-debug.hpp"


//----------------------------------------------------------------------
int main()
{
    uint64_t foo = 0xFFEEDDCC12345678;
    PrintDebug::print_mem_bytes(&foo, sizeof(foo));
    return 0;
}