mutable struct Node # eine veränderbare Datenstruktur
    key::Int # Schlüsselswert
    #Union{A, B} sagt, dass der Wert vom Typ A oder B sein darf
    left::Union{Node, Nothing} # linke Kind
    right::Union{Node, Nothing} # rechte Kind
end

# const = Konstante Bindung, MaybeNode wird nicht mehr neu zugewiesen
const MaybeNode = Union{Node, Nothing}

"""
    node(key::Int)

Erstellt einen neuen Knoten mit dem Wert `key`. Hat keine Kinder

Laufzeit: O(1)
Weil es nur einen Knoten erstellt

# Beispiel
```julia
 julia> x = node(1)
 Node(1, nothing, nothing)
 julia> y = node(2)
 Node(2, nothing, nothing)
```
"""
function node(key::Int)
    return Node(key, nothing, nothing) 
end

"""
    node(key::Int, left::MaybeNode, right::MaybeNode)

Erstellt einen Knoten mit `key`, linkem und rechtem Kind

Laufzeit: O(1)
Weil es nur einen Knoten erstellt

# Beispiel
```julia
 julia> z = node(3, x, y)
 Node(3, Node(1, nothing, nothing), Node(2, nothing, nothing))
```
"""
function node(key::Int, left::MaybeNode, right::MaybeNode)
    return Node(key, left, right)
end

"""
    getKeys(node::Node)::Vector{Int}

Gibt alle Keys aus dem Baum zurück. Reihenfolge: key, links, rechts
Für das linke Kind, wenn node.left nicht leer ist, wird die Funktion getKeys rekursiv fur left ausgeführt
Für das rechte Kind, wenn node.right nicht leer ist, wird die Funktion getKeys rekursiv fur right ausgeführt

Laufzeit: O(n), wobei n die Anzahl der Knoten im Baum ist
Weil jeder Knoten einmal besucht wird


# Beispiel
```julia
 julia> getKeys(z)
 3-element Vector{Int64}:
 3
 1
 2
```
"""
function getKeys(node::Node)::Vector{Int}
    left_keys = Int[]

    if node.left !== nothing
        left_keys = getKeys(node.left)
    end

    right_keys = Int[]
    if node.right !== nothing
        right_keys = getKeys(node.right)
    end

    return [node.key; left_keys; right_keys]
end

"""
    height(node::Node)::Int

Gibt die Höhe des Baums zurück. Ein leerer Baum hat eine Höhe von 0
Die Höhe eines Knotens ist 1 plus die maximale Höhe seiner Kinder
Für das linke Kind, wenn node.left nicht leer ist, wird die Funktion height rekursiv fur left ausgeführt
Für das rechte Kind, wenn node.right nicht leer ist, wird die Funktion height rekursiv fur right ausgeführt

Laufzeit: O(n)
Weil jeder Knoten einmal besucht wird

# Beispiel
```julia
 julia> height(z)
 2
```
"""
function height(node::Node)::Int
    left_height = 0
    if node.left !== nothing
        left_height = height(node.left)
    end

    right_height = 0
    if node.right !== nothing
        right_height = height(node.right)
    end

    return 1 + max(left_height, right_height)
end

"""
    tree2vec(node::Node)::Vector{Union{Int, Nothing}}
Gibt den Baum als Vektor zurück
Wenn die Höhe ist beispeilsweise 3, ist die Reihenfolge mit der rekursiv angerufte Funktion _fillvec wie folgt:
- Wurzel [n=1]
- linkes Kind [n=2]
- linkes Kind des linken Kindes [n=4]
- rechtes Kind des linken Kindes [n=5]
- rechtes Kind [n=3]
- linkes Kind des rechten Kindes [n=6]
- rechtes Kind des rechten Kindes [n=7]

Laufzeit: height(node)[O(n)] + _fillvec(node, n)[O(n)] = O(n)

# Beispiel
```julia
 julia> u = node(4, z, nothing)
 Node(4, Node(3, Node(1, nothing, nothing), Node(2, nothing, nothing)), nothing)
 
 julia> tree2vec(u)
 7-element Vector{Union{Nothing, Int64}}:
 4
 3
 nothing
 1
 2
 nothing
 nothing
```
"""
function tree2vec(node::Node)::Vector{Union{Int, Nothing}}

    vec = Vector{Union{Int, Nothing}}(fill(nothing, 2^height(node)- 1))
    
    function _fillvec(node::MaybeNode, n::Int)
    # _fillvec traversiert den Binärbaum rekursiv
    # An jeder Position n wird der key des Knotens in den Vektor vec eingetragen
    # Die Kinder werden an den Positionen 2n (links) und 2n+1 (rechts) rekursiv eingefügt

    # Laufzeit: O(n)

        if node !== nothing && n <= length(vec)
            vec[n] = node.key
            _fillvec(node.left, 2n)
            _fillvec(node.right, 2n + 1)
        end
    end

    _fillvec(node, 1)

    return vec
end

"""
    vec2tree(vec::Vector{Union{Int,Nothing}}, n::Int=1)::MaybeNode

Erstellt einen Baum aus einem Vektor. 
Der Vektor muss die gleiche Länge wie die Höhe des Baums haben

Laufzeit: O(n), weil jeder Knoten einmal besucht wird

# Beispiel
```julia
julia> vec2tree([4,3,nothing,1,2,nothing,nothing])
 Node(4, Node(3, Node(1, nothing, nothing), Node(2, nothing, nothing)), nothing)
```
"""

function vec2tree(vec::Vector{Union{Int,Nothing}}, n::Int=1)::MaybeNode
    
    # || ist ein Oder operator
    if n > length(vec) || vec[n] === nothing
        return nothing
    end
    
    left_index = 2 * n
    right_index = 2 * n + 1
    
    # rekursive Aufrufe für linkes und rechtes Kind
    # return Node(key, left, right) gibt einen neuen Knoten zurück
    return Node(vec[n], vec2tree(vec, left_index), vec2tree(vec, right_index))
end