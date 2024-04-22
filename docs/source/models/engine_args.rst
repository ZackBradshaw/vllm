.. _engine_args:

Engine Arguments
================

Below, you can find an explanation of every engine argument for vLLM:

.. argparse::
    :module: vllm.engine.arg_utils
    :func: _engine_args_parser
    :prog: -m vllm.entrypoints.openai.api_server
<<<<<<< HEAD
    :nodefaultconst:
=======
>>>>>>> 682789d (Fix missing docs and out of sync `EngineArgs` (#4219))

Async Engine Arguments
----------------------

Below are the additional arguments related to the asynchronous engine:

.. argparse::
    :module: vllm.engine.arg_utils
    :func: _async_engine_args_parser
<<<<<<< HEAD
    :prog: -m vllm.entrypoints.openai.api_server
    :nodefaultconst:
=======
    :prog: -m vllm.entrypoints.openai.api_server
>>>>>>> 682789d (Fix missing docs and out of sync `EngineArgs` (#4219))
