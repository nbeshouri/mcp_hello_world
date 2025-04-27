{
    "messages": [
        HumanMessage(
            content="what's (3 + 5) x 12?",
            additional_kwargs={},
            response_metadata={},
            id="f498d9cf-7839-41d9-9e46-8a35b08dd8e3",
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_GR3meT4CCcjCMnCSZPy2HDFD",
                        "function": {"arguments": '{"a": 3, "b": 5}', "name": "add"},
                        "type": "function",
                    },
                    {
                        "id": "call_91xB2pNlNxB8NYbLBDJFZVQ5",
                        "function": {
                            "arguments": '{"a": 12, "b": 1}',
                            "name": "multiply",
                        },
                        "type": "function",
                    },
                ],
                "refusal": None,
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 51,
                    "prompt_tokens": 77,
                    "total_tokens": 128,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-mini-2024-07-18",
                "system_fingerprint": "fp_64e0ac9789",
                "id": "chatcmpl-BQmolLp7HKLBHC2o234N08yQUN5Ww",
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            id="run-15ebd95d-839f-4e3f-b9bf-c46919d3480e-0",
            tool_calls=[
                {
                    "name": "add",
                    "args": {"a": 3, "b": 5},
                    "id": "call_GR3meT4CCcjCMnCSZPy2HDFD",
                    "type": "tool_call",
                },
                {
                    "name": "multiply",
                    "args": {"a": 12, "b": 1},
                    "id": "call_91xB2pNlNxB8NYbLBDJFZVQ5",
                    "type": "tool_call",
                },
            ],
            usage_metadata={
                "input_tokens": 77,
                "output_tokens": 51,
                "total_tokens": 128,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
        ToolMessage(
            content="8",
            name="add",
            id="612c4345-ef3e-4867-8c4d-5baada558adc",
            tool_call_id="call_GR3meT4CCcjCMnCSZPy2HDFD",
        ),
        ToolMessage(
            content="12",
            name="multiply",
            id="3d366585-0bc0-477c-84bb-f9d56ee36407",
            tool_call_id="call_91xB2pNlNxB8NYbLBDJFZVQ5",
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_fKg6DWX3f4orhc9AP9iz42Q7",
                        "function": {"arguments": '{"a":8,"b":12}', "name": "multiply"},
                        "type": "function",
                    }
                ],
                "refusal": None,
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 18,
                    "prompt_tokens": 143,
                    "total_tokens": 161,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-mini-2024-07-18",
                "system_fingerprint": "fp_64e0ac9789",
                "id": "chatcmpl-BQmompdYsnFsP4n6gO1RaJMHiElQC",
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            id="run-22fc5bc4-d2de-4c47-afe9-0c2cae886ca0-0",
            tool_calls=[
                {
                    "name": "multiply",
                    "args": {"a": 8, "b": 12},
                    "id": "call_fKg6DWX3f4orhc9AP9iz42Q7",
                    "type": "tool_call",
                }
            ],
            usage_metadata={
                "input_tokens": 143,
                "output_tokens": 18,
                "total_tokens": 161,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
        ToolMessage(
            content="96",
            name="multiply",
            id="9b438d8c-9db9-422e-bd40-d027594ab49e",
            tool_call_id="call_fKg6DWX3f4orhc9AP9iz42Q7",
        ),
        AIMessage(
            content="The result of \\((3 + 5) \\times 12\\) is 96.",
            additional_kwargs={"refusal": None},
            response_metadata={
                "token_usage": {
                    "completion_tokens": 22,
                    "prompt_tokens": 168,
                    "total_tokens": 190,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-mini-2024-07-18",
                "system_fingerprint": "fp_64e0ac9789",
                "id": "chatcmpl-BQmonaEh8ORpbHSL06HNiCjLmVC1p",
                "finish_reason": "stop",
                "logprobs": None,
            },
            id="run-0501fb00-3b8e-4229-b8fa-07b891a4fd5e-0",
            usage_metadata={
                "input_tokens": 168,
                "output_tokens": 22,
                "total_tokens": 190,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
    ]
}
