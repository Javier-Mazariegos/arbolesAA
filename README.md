# arbolesAA
Los arboles AA son un tipo de árbol binario de busqueda autobalanceable, es una variación del árbol rojo-negro y una mejora del árbol binario de búsqueda. Su principal característica es almcenar y recuperar información ordenada de forma eficiente. Al ser un arbol autobalanceable necesita mantenerse en equilibrio por medio de dos operaciones llamadas skew y split. 

Un skew es una rotación derecha que pasa cuando se realiza un insert o un delete que genera un enlace horizontal izquierdo. Un split es una rotación izquierda que pasa cuando se realiza un insert o un delete genera dos enlaces horizontales derechos. 

Para que el árbol AA sea valido, necesita cumplir con las siguientes condiciones:
1. El nivel de un nodo hoja es uno.
2. El nivel de un hijo izquierdo es estrictamente menor que el de su padre.
3. El nivel de un hijo derecho es menor o igual que el de su padre.
4. El nivel de un nieto derecho es estrictamente menor que el de su abuelo.
5. Cada nodo de nivel mayor que uno debe tener dos hijos.

#Profiling
![image](https://user-images.githubusercontent.com/61554803/114329456-a07e4d00-9afc-11eb-8d93-6c37f4ea79be.png)
