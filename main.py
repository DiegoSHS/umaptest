import numpy
import streamlit as st
from matplotlib import pyplot as plt
from threading import _RLock
from umap import umap_


def main():
    """This function runs UMAP on a random dataset and plots the results."""
    menssage = """
    Este es un ejemplo de un plot de UMAP
    creado para una expo de muestra, la base de código
    es propiedad de CADELmx
    """
    st.header("UMAP plot")
    st.write(menssage)
    data = numpy.random.rand(100, 10)
    reducer = umap_.UMAP()
    embedding = reducer.fit_transform(data)
    with _RLock() as _:
        fig, ax = plt.subplots()
        ax.set_title("UMAP plot")
        ax.scatter(embedding[:, 0], embedding[:, 1])
        st.pyplot(fig)
    st.write("Codigo de esta webapp:")
    st.code(to_string())
        
        
def to_string():
    """This function returns the code of the main function as a string."""
    with open("main.py", "r") as file:
        return file.read()


main()