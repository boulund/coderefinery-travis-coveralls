#!/usr/bin/env python
import pytest

def return2():
    return 2
    
def test_return2():
    assert(return2() == 0)
