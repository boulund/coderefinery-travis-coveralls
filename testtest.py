#!/usr/bin/env python
import pytest

def return2(n):
    if n:
        return 2
    else:
        return 1
    
def test_return2():
    assert(return2(1) == 2)
