import sys

import pytest

from boilerplate.boilerplate import Boilerplate, cli, clparser


def run_clparser(args):
    """Run the command line argument parser."""
    sys.argv = ["boilerplate.py", *args]
    return clparser()


def test_version(capsys):
    """Test the argument parser version flag."""
    with pytest.raises(SystemExit):
        run_clparser(["--version"])
    captured = capsys.readouterr()
    assert "boilerplate.py 0.0.1" in captured.out


def test_debug(capsys):
    """Test the argument parser debug flag."""
    args = run_clparser(["2", "2"])
    assert not args.debug
    args = run_clparser(["-d", "2", "2"])
    assert args.debug


def test_verbose(capsys):
    """Test the argument parser verbose flag."""
    args = run_clparser(["2", "2"])
    assert not args.verbose
    args = run_clparser(["-v", "2", "2"])
    assert args.verbose


def test_positional_args():
    """Test the argument parser positional arguments."""
    args = run_clparser(["2", "2"])
    assert args.x == 2
    assert args.y == 2


def test_cli_not_verbose(capsys):
    """Test the cli without verbose mode."""
    run_clparser(["2", "2"])
    cli()
    captured = capsys.readouterr()
    assert captured.out == ""


def test_cli_verbose(capsys):
    """Test the cli without verbose mode."""
    run_clparser(["-v", "2", "2"])
    cli()
    captured = capsys.readouterr()
    assert "Boilerplate(x=2.0, y=2.0)" in captured.out
    assert "Add: 4.0" in captured.out
    assert "Subtract: 0.0" in captured.out
    assert "Multiply: 4.0" in captured.out
    assert "Divide: 1.0" in captured.out


def test_boilerplate_ints() -> None:
    """Test the Boilerplate class with integers."""
    boilerplate = Boilerplate(2, 2)
    assert boilerplate.x == 2
    assert boilerplate.y == 2
    assert str(boilerplate) == "Boilerplate(x=2, y=2)"
    assert boilerplate.add() == 4
    assert boilerplate.subtract() == 0
    assert boilerplate.multiply() == 4
    assert boilerplate.divide() == 1.0
    assert Boilerplate(2, 0).divide() == "Cannot divide by zero."


def test_boilerplate_floats() -> None:
    """Test the Boilerplate class with floats."""
    boilerplate = Boilerplate(2.5, 2.5)
    assert boilerplate.x == 2.5
    assert boilerplate.y == 2.5
    assert str(boilerplate) == "Boilerplate(x=2.5, y=2.5)"
    assert boilerplate.add() == 5.0
    assert boilerplate.subtract() == 0.0
    assert boilerplate.multiply() == 6.25
    assert boilerplate.divide() == 1.0
    assert Boilerplate(2, 0).divide() == "Cannot divide by zero."
