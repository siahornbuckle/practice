/***********************************************************************
 *   ____   ___    _
 *  / ___| |_ _|  / \
 *  \___ \  | |  / _ \
 *   ___) | | | / ___ \
 *  |____/ |___/_/   \_\
 *
 *  File:        test-print.cpp
 *  Author:      SIA
 *  Description: <brief description of the file>
 *  Created:     <date>
 **********************************************************************/

#include <stdint.h>
#include "print-debug.hpp"


//----------------------------------------------------------------------
int main()
{
    int8_t foo = -1;
    uint8_t bar = 255;
    //PrintDebug::print_mem_bytes(&foo, sizeof(foo), "foo");
    PrintDebug::print_mem_bytes(&bar, sizeof(bar), "bar");
    return 0;
}