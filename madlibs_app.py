import streamlit as st

st.title("Mad Libs: There Was an Old Lady...")

st.write("Fill in the blanks below to create your custom story.")

fly = st.text_input("Enter a tiny thing")
reaction = st.text_input("Enter a reaction")
spider = st.text_input("Enter a gross creature")
squirmy_action = st.text_input("Enter a squirmy action")
bird = st.text_input("Enter a bird-type animal")
cat = st.text_input("Enter a household pet")
dog = st.text_input("Enter a wild animal")
cow = st.text_input("Enter a farm animal")
horse = st.text_input("Enter a final creature or object")

if st.button("Generate Story"):
    st.markdown(f"""
There was an old lady who swallowed a {fly}  
I don't know why she swallowed a {fly} — perhaps she'll {reaction}!

There was an old lady who swallowed a {spider},  
That {squirmy_action} inside her;  
She swallowed the {spider} to catch the {fly};  
I don't know why she swallowed a {fly} — perhaps she'll {reaction}!

There was an old lady who swallowed a {bird};  
How absurd to swallow a {bird}.  
She swallowed the {bird} to catch the {spider},  
She swallowed the {spider} to catch the {fly};  
I don't know why she swallowed a {fly} — perhaps she'll {reaction}!

There was an old lady who swallowed a {cat};  
Fancy that to swallow a {cat}!  
She swallowed the {cat} to catch the {bird},  
She swallowed the {bird} to catch the {spider},  
She swallowed the {spider} to catch the {fly};  
I don't know why she swallowed a {fly} — perhaps she'll {reaction}!

There was an old lady who swallowed a {dog};  
What a hog, to swallow a {dog};  
She swallowed the {dog} to catch the {cat},  
She swallowed the {cat} to catch the {bird},  
She swallowed the {bird} to catch the {spider},  
She swallowed the {spider} to catch the {fly};  
I don't know why she swallowed a {fly} — perhaps she'll {reaction}!

There was an old lady who swallowed a {cow},  
I don't know how she swallowed a {cow};  
She swallowed the {cow} to catch the {dog},  
She swallowed the {dog} to catch the {cat},  
She swallowed the {cat} to catch the {bird},  
She swallowed the {bird} to catch the {spider},  
She swallowed the {spider} to catch the {fly};  
I don't know why she swallowed a {fly} — perhaps she'll {reaction}!

There was an old lady who swallowed a {horse}...  
She's dead, of course!
""")
