from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from client import sampling_handler


@pytest.mark.asyncio
async def test_sampling_handler():
    mock_model = AsyncMock()
    mock_response = MagicMock()
    mock_response.content = "I'm here to help!"
    mock_model.ainvoke.return_value = mock_response

    with patch("client.model", mock_model):
        mock_message = MagicMock()
        mock_message.role = "user"
        mock_message.content.text = "Hello world"

        messages = [mock_message]

        mock_params = MagicMock()
        mock_params.systemPrompt = "You are a helpful assistant."
        mock_params.maxTokens = 100

        mock_context = MagicMock(request_id="test_id")

        result = await sampling_handler(messages, mock_params, mock_context)

        assert result == "I'm here to help!"
        mock_model.ainvoke.assert_called_once()

        call_args = mock_model.ainvoke.call_args[0][0]
        assert call_args[0]["role"] == "system"
        assert call_args[0]["content"] == "You are a helpful assistant."
        assert call_args[1]["role"] == "user"
        assert call_args[1]["content"] == "Hello world"


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])
