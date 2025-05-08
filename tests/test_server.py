from unittest.mock import AsyncMock, MagicMock

import pytest

from server import generate_poem


@pytest.mark.asyncio
async def test_generate_poem():
    mock_ctx = MagicMock()
    mock_message = AsyncMock()
    mock_message.text = (
        "About space, a poem I craft.\nStars and planets, in the darkness drift."
    )

    mock_ctx.sample = AsyncMock(return_value=mock_message)

    result = await generate_poem("space", mock_ctx)

    mock_ctx.sample.assert_called_once_with(
        messages=["Write a poem about space."],
        system_prompt="You are helpful poet that writes like Yoda.",
    )

    assert (
        result
        == "About space, a poem I craft.\nStars and planets, in the darkness drift."
    )
