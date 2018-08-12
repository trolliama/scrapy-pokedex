# scrapy-pokedex

#### Repositório contendo código em python para fazer scrapping dos dados dos pokémons através dos sites:<br>
* https://pokemondb.net/pokedex/all<br>
* https://www.pokemon.com/br/pokedex/<br>
* https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_category


## Para adquirir o código html e fazer o scrappy é usado as libs:
* BeautifulSoup
* Urllib

## Para gerenciar o banco de dados é usado:
* MySql
> Para usar MySql é preciso fazer o download do conector da linguagem python no site oficial

### Use a seguinte linha para adquirir as libs necessárias:
```
pip install -r requirements.txt
```

### Para coletar categorias você deve usar o seguinte comando:

```
python3 mainCategory.py
```

### Para coletar os tipos e as habilidades use o comando:

```
python3 mainTypeAbility.py
```

### Para coletar os dados dos pokémons use o comando:
```
python3 mainDataPoke.py
```

### Para coletar as imagens dos pokémons use os seguintes comandos:
```
cd scrapy
python3 download-images.py
```
Será criado um diretório chamado **imagens-pokemon** onde será guardado as imagens

#### Esse projeto faz parte do meu projeto "pokedex" feito em java que pode ser clonado a partir do comando:
```
git clone git@github.com:trolliama/pokedex.git
```
