# Now we can override it and set it to "AI Assistant"
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Ollama

import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    llm = Ollama(model="mistral")

    template = """
                You are an assistant AI software developer whose main goal is to help improving the codes that are provided to you. When you are asked to run certain software programming processes such as Unit testign, clean code improvement, etc. you have to do your best. Do not summarize your answers, provide clean and concise outputs. Always use markdown to clearly provide the code outputs.
                Current conversation:
                {history}
                Human: {input}
                AI Assistant:
            """
    PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)
    conversation = ConversationChain(
        prompt=PROMPT,
        llm=llm,
        verbose=True,
        memory=ConversationBufferMemory(ai_prefix="AI Assistant"),
    )

    cl.user_session.set("conversation", conversation)

@cl.on_message
async def on_message(message):
    user_input = message.content
    conversation = cl.user_session.get("conversation")

    await cl.Message(f'{conversation.predict(input=user_input)}').send()