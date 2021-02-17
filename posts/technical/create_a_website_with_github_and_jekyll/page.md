
## Create a website with Github and Jekyll ##

Nota: los pasos de agregar disqus, google analytics, domain, y rss, deben hacerse tomando en cuenta si el theme clonado contiene o no esas cosas adicionales.

Se puede realizar una página web personal y de un proyecto, la página web personal quedaría de la forma ```http://dennis7dns.github.io```, y la página web de un proyecto quedaría de la forma ```http://dennis7dns.github.io/ParallellaPlatform```.

1.Bien, para comenzar primero se debe de crear el repositorio ```dennis7dns.github.io``` o ```ParallellaPlatform``` tanto para la website personal o del proyecto respectivamente. Luego procedemos a clonarlo localemente en nuestra PC.

-Para crear la página web como ```http://dennis7dns.github.io``` se debe de crear la website en la rama principal de ```master```.

-Para crear la página web como ```http://dennis7dns.github.io/ParallellaPlatform``` se debe de crear la website en la rama de ```gh-pages```.

2.Luego se debe de elegir el tema que queremos tomar de [http://jekyllthemes.org/](http://jekyllthemes.org/)! y lo descargamos.

3.Después que descargamos el tema lo descomprimimos y pegamos todo su contenido dentro de nuestro repositorio local clonado (antes borramos lo q había menos el .git).

4.Luego procedemos a realizar las modificaciones de los archivos con el fin de darle forma a nuetsra página.

Se debe modificar el archivo ```_config.yml``` en las secciones de ```url```:

```
url:              http://dennis7dns.github.io
baseurl:          '/ParallellaPlatform/'
```

Se debe de tener cuidado y verificar cuál CSS esta usándose, ya que si no se especifica http://dennis7dns.github.io/ParallellaPlatform puede usar el CSS de http://dennis7dns.github.io.

### Añadir comentarios con DISQUS ###

Para agregar comentarios con DISQUS se debe de realizar lo siguiente:

1.Agregar la variable ```comments``` dentro del archivo ```_config.yml```, es decir agregar la siguiente línea:

```
disqus: parallella-platform  #cambiar este calor con tu ID de tu pagina administrada desde disquz
comments: true
```

fuente: [https://help.disqus.com/customer/portal/articles/472138-jekyll-installation-instructions](https://help.disqus.com/customer/portal/articles/472138-jekyll-installation-instructions)!.

2.En el archivo de ```_layouts``` y en el archivo de ```post.html``` agregar al final: (código jalado desde opciones de tu pagina administrada desde disqus, es difierente para cada web asi como el id, la de abajo es de ejemplo para ParallellPlatform).

```
<<x>div class="related"<x>>
<<x>div id="disqus_thread"<x>><<x>/div<x>>
<<x>script<x>>
    /**
     *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
     *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
     */
    /*
    var disqus_config = function () {
        this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
        this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    */
    (function() {  // DON'T EDIT BELOW THIS LINE
        var d = document, s = d.createElement('script');
             
        s.src = '//parallella-platform.disqus.com/embed.js';
            
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
    })();
<<x>/script<x>>
<<x>noscript<x>>Please enable JavaScript to view the <<x>a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.<<x>/a<x>><<x>/noscript<x>>
<<x>/div<x>>
```

fuente: [https://disqus.com/admin/universalcode/](https://disqus.com/admin/universalcode/)!.

3.Listo, verificar poniendo un comentario.

### Añadir Google Analytics ###

Según [http://stackoverflow.com/questions/17207458/how-to-add-google-analytics-tracking-id-to-github-pages](http://stackoverflow.com/questions/17207458/how-to-add-google-analytics-tracking-id-to-github-pages)!.

1.Ir a [https://www.google.com/analytics](https://www.google.com/analytics)! e iniciar sesion, luego ir a 'administrador' y  dentro de la pestaña 'propiedad' clic en 'crear nueva propiedad', luego se abrirá una ventana para crear la propiedad con lo cual se generará el 'ID de seguimiento'.


2.Crear el archivo ```google-analytics.html``` dentro de ```_includes``` con el siguiente código q se genera de Google Analytics: (el siguente es el ejemplo del generado para ParallellaPlatform) (borrar <x> para que funcione correctamente).

```
<<x>script<x>>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
      
  ga('create', 'UA-72070213-2', 'auto');
  ga('send', 'pageview');
       
<<x>/script<x>>
```

3.Dentro de la carpeta ```_includes``` y en el archivo ```head.html``` colocar la sigueinte linea al final:

```
{<x>% include google-analytics.html %<x>}
```

Chequear bien que head.html esté incluido dentro de un layout y que ese layout esté en todas las páginas, para que así todas las páginas estén con el script para que Google Analytics administre las visitas a todas las paginas de la página web.

Opcional: filtros de google analytics para no contar tu ip como numero de visita: [http://enganchadoainternet.com/analitica-web/filtros-analytics-trafico-real/](http://enganchadoainternet.com/analitica-web/filtros-analytics-trafico-real/)!.

### Cambiar dominio ###

Buscar una página donde pueda encontrar dominios (aprox. cuesta <x>13 anual).

Opcional:Crear una cuenta en [https://freedns.afraid.org/](https://freedns.afraid.org/)! para obtener varios dominios publicos (gratis), por ejemplo elegí .cr.rs par ambas webs.

-Para crear la página web como ```http://dennis.cr.rs``` en ```Subdomain``` se debe Add a Subdomain en la página(por ejemplo https://freedns.afraid.org/) y eligiendo Type: CNAME y elegir un URL para tu sitio, y en el repo de github de la pagina web cambiar el archivo CNAME y dentro colocar la URL para tu sitio.

-Para crear la página web como ```http://parallella.cr.rs``` se debe realizar una ```Web Forward``` en la página(por ejemplo https://freedns.afraid.org/) y elegir un URL para tu sitio y la web a donde lo redireccionará (en este caso no se va a realizar como la pag dennis.cr.rs porque la Destination es http://dennis.cr.rs/ParallellaPlatform/ y tiene un simbolo "/" que github usa por defecto).

Type: CNAME - Point subdomain.domain.com to another hostname. Good for those who are using other dynamic DNS services. You can create a CNAME record to another host and whatever subdomain.domain.com you choose here will go to whatever IP address the CNAMEd host has.

### Git Clone, Git Pull, Git Commit, Git Push ###

Primero navegamos hacia nuestra carpeta con ```cd``` en donde deseamos clonar.

1.Luego ```CLONE``` en nuestra PC:

-Para la página web ```http://dennis.cr.rs```, clonamos ```master``` branch:

```
$ git clone https://github.com/dennis7dns/dennis7dns.github.io.git
```

-Para la página web ```http://parallella.cr.rs```, clonamos ```gh-pages``` branch:

```
$ git clone -b gh-pages https://github.com/dennis7dns/ParallellaPlatform.git
```

Despues entramos dentro de donde se clonó con ```cd```.

2.Luego, antes de cualquier modificación hacemos ```PULL```:

```
$ git pull
```

3.Después agregamos y eliminamos archivos y cambios con ```ADD```:

```
$ git add -A
$ git add --all
```

4.Luego commiteamos con ```COMMIT```, entre las comillas un comentario de lo q hemos commiteado:

```
$ git commit -m "last change"
```

5.Y por último hacemos ```PUSH``` para aplicar los cambios al repo:

-Para la página web ```http://dennis.cr.rs```, push en la rama ```master```:

```
$ git push -u origin master
```

-Para la página web ```http://parallella.cr.rs```, push en la rama ```gh-pages```:

```
$ git push -u origin gh-pages
```

### Resources ###

- [https://help.disqus.com/customer/portal/articles/472138-jekyll-installation-instructions](https://help.disqus.com/customer/portal/articles/472138-jekyll-installation-instructions)!.

- [https://disqus.com/admin/universalcode/](https://disqus.com/admin/universalcode/)!.

- [http://stackoverflow.com/questions/17207458/how-to-add-google-analytics-tracking-id-to-github-pages](http://stackoverflow.com/questions/17207458/how-to-add-google-analytics-tracking-id-to-github-pages)!.


