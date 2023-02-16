# same as agent.py except!

## 
## Remembers memory based on the indivdiual Zulip ID being different.

digital_twins = {
    "user1@aol.xyz": "memory1 object",
    "user2@aol.xyz": "memory2 object ",
}

## Script:
## Immediate term: ask Unhack gm_agent to summarize values for each digital_twin towards the end of the conversation and say does anything on this list look like it doesn't belong or would you change anything?

## Stage 0: Elicitation

## Example:
## > What is your favorite writing?
##  <https://chiaski.github.io/poeticweb/ text from the top>
## Prompt: List 5 bulleted moral, political, economic, environmental values that I am likely to have.
##
## Output:
## Appreciation for creativity and self-expression through art and poetry (moral value).
## Belief in the importance of community and collaboration, as evidenced by the links to student work and shared resources (political value).
## Emphasis on the power of technology and digital platforms, as demonstrated by the use of HTML/CSS/JS and the inclusion of online resources (economic value).
## Recognition of the impact of human actions on the environment, as evidenced by the interest in exploring "softer digital futures" and creating a "poetic web" (environmental value).
## Promotion of inclusivity and diversity through the open invitation to students and the sharing of a variety of resources (moral and political value).

## do this for everyone

## Stage 1: Aggregation

## Prompt:
##We have Alice, whose elicited values are these:
##Appreciation for creativity and self-expression through art and poetry (moral value).
##Belief in the importance of community and collaboration, as evidenced by the links to student work and shared resources (political value).
##Emphasis on the power of technology and digital platforms, as demonstrated by the use of HTML/CSS/JS and the inclusion of online resources (economic value).
##Recognition of the impact of human actions on the environment, as evidenced by the interest in exploring "softer digital futures" and creating a "poetic web" (environmental value).
##Promotion of inclusivity and diversity through the open invitation to students and the sharing of a variety of resources (moral and political value).

## Bob, whose elicited values are these:
#Civil liberties: As a special consultant to the Electronic Frontier Foundation (EFF), Cory Doctorow is likely to value civil liberties, including freedom of expression and privacy, particularly as they relate to technology and the internet.
# Anti-monopoly: Doctorow's recent book CHOKEPOINT CAPITALISM, co-authored with Rebecca Giblin, suggests a concern with the negative effects of monopolies on creative labor markets. He may therefore value competition and oppose the concentration of economic power in a few large corporations.
# Science fiction and technology: As a science fiction author and technology activist, Doctorow is likely to value innovation and the potential of technology to shape the future. He may also be interested in exploring the ethical and social implications of emerging technologies in his work.
# Environmentalism: While Doctorow's work doesn't directly address environmental issues, his concern with the future and the impact of technology on society may suggest a value for sustainability and ecological responsibility.
# Open source and peer-to-peer: Doctorow's involvement in the open source and peer-to-peer software communities through his work with OpenCola and advisory board positions suggests a value for decentralized, collaborative approaches to technology development and distribution. He may see these approaches as more democratic and equitable than proprietary systems.
## 


## and Carol, whose elicited values are these:
# Fair compensation for individuals who contribute their data to AI models
# Individual control over how their data is used
# Ethical and transparent use of data
# Opposition to exploitation of individuals' data without their consent or compensation
# Recognition of the potential impact of AI models on workers and the importance of addressing this issue through collective solutions


# Stage 2: Coalition Formation - suggest coalitions
# {Alice, Bob, Carol} - This coalition would have a broad range of values to draw from and could potentially create a well-rounded and dynamic project. They share an interest in technology, innovation, and ethical responsibility, but also value inclusivity, individual rights, and environmental sustainability. However, given their diverse values and priorities, they may have to work harder to find common ground and ensure everyone's values are respected.

# {Alice, Bob} and {Carol} - This grouping could be beneficial as Alice and Bob share an interest in technology, digital platforms, and the impact of human actions on the environment. Carol's values on individual rights and ethical use of data align with those of Alice and Bob, but she also brings a unique perspective on fair compensation for data use and the impact of AI on workers. However, this coalition may lack the collaboration and inclusivity values that Alice holds dear.

# {Alice, Carol} and {Bob} - This coalition shares an emphasis on individual rights, ethical and transparent use of data, and the importance of addressing the impact of technology on society. However, they may lack the technical expertise and interest in innovation and creativity that Bob brings to the table, potentially limiting the scope of their project.

# {Alice} and {Bob, Carol} - This grouping may struggle to find common ground as Alice's values emphasize collaboration and creativity, while Bob and Carol's values focus more on individual rights and responsible data use. This coalition may need to work hard to balance these values and ensure that everyone's priorities are represented in their project.

# {Alice}, {Bob}, and {Carol} working independently - While each individual brings valuable perspectives and expertise, working independently could limit the potential for collaboration and could result in a disjointed final project. This coalition may need to find a way to coordinate and share their work to ensure that their individual efforts result in a cohesive whole.

# Overall, the coalition of {Alice, Bob, Carol} may be the most likely to lead to a successful project as they have the broadest range of values to draw from, though any of these groupings could work if everyone is willing to communicate and compromise. It's important for each person to be aware of their own values and priorities as well as those of their coalition members, and to work together to create a project that reflects everyone's contributions and perspectives.

# Stage 3: Coalitions are formed and the open game begins
# - ...
# - ... ????


# Stage 4: Social Simulation
# - (at some point of the game) agents will try to convince other coalition members to switch
# Assuming the coalition alignment is {{Alice, Bob}, {Carol, Duke}}, here are some possible reasons or motivations that Alice and Bob could use to convince Carol or Duke to switch coalitions:

# Alice and Bob could highlight their shared values with Carol, such as their belief in the importance of community and collaboration, promotion of inclusivity and diversity, and recognition of the impact of human actions on the environment. They could argue that this alignment better reflects Carol's values and priorities than her current alignment with Duke.

# Alice and Bob could emphasize their technical expertise and interest in innovation and creativity, which may align more closely with Duke's values than Carol's. They could argue that Duke would have more opportunities to contribute in this area in their coalition.

# On the other hand, Carol and Duke could use the following reasons or motivations to convince Alice and Bob to switch coalitions:

# Carol and Duke could argue that their alignment better reflects Bob's values and priorities, given that Duke is an identical digital twin of Bob's. They could emphasize their shared values with Bob, such as civil liberties, opposition to exploitation of individuals' data without their consent or compensation, and recognition of the potential impact of AI models on workers.

# Carol and Duke could highlight their emphasis on fair compensation for individuals who contribute their data to AI models, individual control over how their data is used, and ethical and transparent use of data, which may not align as closely with Alice's values as with Carol and Duke's. They could argue that Alice would have more opportunities to contribute in these areas in their coalition.

# Stage 5: Propaganda
# "Hey Alice, I hope you're doing well. I wanted to check in and see if you've thought about teaming up with Carol and Duke for this project. I know it's a tough time for you, but if you're up for it, they'd be a great group to work with. They value ethical data use and fair compensation, and Duke's got some serious tech skills that could come in handy. Let me know if you want to talk more about it. Take care."
