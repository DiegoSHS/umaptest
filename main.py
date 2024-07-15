import numpy
import streamlit as st
from matplotlib import pyplot as plt
from threading import _RLock
from umap import umap_


def main():
    """This function runs UMAP on a random dataset and plots the results."""
    st.header("UMAP plot")
    st.write("Este es un ejemplo de un plot de UMAP creado para una expo de muestra, la base de codigo es propiedad de CADELmx")
    data = numpy.random.rand(100, 10)
    reducer = umap_.UMAP()
    embedding = reducer.fit_transform(data)
    with _RLock() as _:
        fig, ax = plt.subplots()
        ax.set_title("UMAP plot")
        ax.scatter(embedding[:, 0], embedding[:, 1])
        st.pyplot(fig)
        
main()