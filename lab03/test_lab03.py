
import pytest
from lab03.lab03 import generate_mad_lib

def test_generate_mad_lib_basic():
	result = generate_mad_lib("silly", "cat", "jumped")
	assert "silly cat jumped" in result

def test_generate_mad_lib_custom():
	result = generate_mad_lib("brave", "knight", "battled")
	assert "brave knight battled" in result

