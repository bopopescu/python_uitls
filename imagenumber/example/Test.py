


from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)
text = open(path.join(d, 'alice.txt')).read()
alice_mask = np.array(Image.open(path.join(d, "alice_color.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords)
wc.generate(text)
wc.to_file(path.join(d, "alice1112.png"))





# d = path.dirname(__file__)
#
# # Read the whole text.
# text = open(path.join(d, 'constitution.txt')).read()
#
# # Generate a word cloud image
# wordcloud = WordCloud().generate(text)
#
# # Display the generated image:
# # the matplotlib way:
# import matplotlib.pyplot as plt
# plt.imshow(wordcloud)
# plt.axis("off")
#
# # take relative word frequencies into account, lower max_font_size
# wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
# plt.figure()
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()