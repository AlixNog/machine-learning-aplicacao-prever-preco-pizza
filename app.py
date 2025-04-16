{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "acd7697f-5869-4c2f-b788-a7955e4c71a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "43e61b01-d8bb-4ff8-81f3-b97d28f59122",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"pizzas.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7dacf29f-620d-4785-9dcd-b28af081689f",
   "metadata": {},
   "outputs": [],
   "source": [
    "modelo = LinearRegression()\n",
    "x=df[[\"diametro\"]]\n",
    "y=df[[\"preco\"]]\n",
    "\n",
    "modelo.fit(x,y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "325696bd-0bf8-41d4-bc47-1b483c495f16",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title(\"prevendo o valor de uma pizza\")\n",
    "st.divider()\n",
    "diametro = st.number_input(\"digite diametro\")\n",
    "\n",
    "if diametro:\n",
    "    preco_previsto = modelo.predict([[diametro]][0][0])\n",
    "    st.write(f\"valor pizza de diametro {diametro} eh de {preco_predict} reais)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "156799c8-477e-4646-a1d5-5304759136e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title(\"prevendo o valor de uma pizza\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac39610d-7a7b-45c7-9d5a-9d3cd2dcdbe3",
   "metadata": {},
   "outputs": [],
   "source": [
    "!streamlit run app.py & npx localtunnel --port 8501"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4be4542e-ad8a-4e62-838b-8fed2b7b3fd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "streamlit run app.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53d20d39-23ed-485b-8f8a-12723c4edb11",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
