#!/usr/bin/env python
import pytest

# https://click.palletsprojects.com/en/7.x/testing/
from click.testing import CliRunner
from disaster_tweets.cli.main import cli

def test_cli():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    help_result = runner.invoke(cli, ['--help'])
    assert help_result.exit_code == 0

def test_predict_via_cli():
    """Test generating a model prediction via the CLI."""
    runner = CliRunner()
    argument = "Theyd probably still show more life than Arsenal did yesterday, eh? EH?"
    result = runner.invoke(cli, ['predict',argument])
    assert result.exit_code == 0, "Predict failed with error: "+ result.output
    assert len(result.output) > 0
