This repository is to be parsed by the [3ID DID](https://developers.ceramic.network/docs/advanced/standards/accounts/3id-did/) capable Plurigraph.

In itself, the Plurigraph is simply a collection of markdown files of this property:
- the paths are relative
- backlink square bracket syntax is used to create edges between nodes quickly while editing text in anything capable of editing text
- ...

# Smart features
https://openai.com/blog/webgpt/
Translation
Fill-Mask
Token Classification
Sentence Similarity
Question Answering
Summarization
Zero-Shot Classification
Text Classification
Text2Text Generation
Text Generation
Conversational
Table Question Answering
# Automating population of graph from text
## Named entity recognition
"Decide what part of the sentence that are important* to turn into their own node and attempt to elaborate what they are from text."

What part of this senence example is likely to confuse a user and require elaboration? The classic named entity recognition task is a good starting point for the first part of mining ontology from the existing corpus.

## Question answering
In order to simplify summarization of our detected named entities, use a simple Question `what is <named entity>` and record a result as the content of the text of the node of the detected entity.