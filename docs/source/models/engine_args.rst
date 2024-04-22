.. _engine_args:

Engine Arguments
================

Below, you can find an explanation of every engine argument for vLLM:

.. argparse::
    :module: vllm.engine.arg_utils
    :func: _engine_args_parser
    :prog: -m vllm.entrypoints.openai.api_server
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    :nodefaultconst:
=======
>>>>>>> 682789d (Fix missing docs and out of sync `EngineArgs` (#4219))
=======
    :nodefaultconst:
>>>>>>> fe7d648 (Don't show default value for flags in `EngineArgs` (#4223))
=======
    :nodefaultconst:
>>>>>>> main

Async Engine Arguments
----------------------

Below are the additional arguments related to the asynchronous engine:

.. argparse::
    :module: vllm.engine.arg_utils
    :func: _async_engine_args_parser
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    :prog: -m vllm.entrypoints.openai.api_server
    :nodefaultconst:
=======
    :prog: -m vllm.entrypoints.openai.api_server
>>>>>>> 682789d (Fix missing docs and out of sync `EngineArgs` (#4219))
=======
    :prog: -m vllm.entrypoints.openai.api_server
    :nodefaultconst:
>>>>>>> fe7d648 (Don't show default value for flags in `EngineArgs` (#4223))
=======
    :prog: -m vllm.entrypoints.openai.api_server
    :nodefaultconst:
>>>>>>> main
