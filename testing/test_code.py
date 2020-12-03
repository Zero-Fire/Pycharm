# -*- coding: utf-8 -*-
import pytest
from Calcu.demo1 import Calculator

def test_add():
    a=Calculator()
    result = a.add(1,1)
    assert result==2
