mutable struct Heap{T <: Real}
    data::Vector{T}
    comparator::Function

    function Heap(data::Vector{T}; comparator::Function)::Heap{T} where T <: Real
        @assert hasmethod(comparator, Tuple{T, T}) "Comparator not defined for type $T"
        ret_types = Base.return_types(comparator, Tuple{T, T})
        @assert all(rt == Bool for rt in ret_types) "Comparator must return Bool"
        new{T}(data, comparator)
    end

    function Heap(data::Vector{T})::Heap{T} where T <: Real
        Heap(data; comparator = ≥)
    end
end

function is__Heap(heap::Heap{T})::Bool where T <: Real
    data = heap.data
    cmp = heap.comparator
    n = length(data)
    for i in 1:div(n, 2)
        l = 2 * i
        r = 2 * i + 1
        if l <= n && !cmp(data[i], data[l])
            return false
        end
        if r <= n && !cmp(data[i], data[r])
            return false
        end
    end
    return true
end

function heapify!(heap::Heap{T})::Heap{T} where T <: Real
    data = heap.data
    cmp = heap.comparator
    function _sift_down!(i)
        n = length(data)
        while 2 * i <= n
            l = 2 * i
            r = 2 * i + 1
            j = i
            if l <= n && cmp(data[l], data[j])
                j = l
            end
            if r <= n && cmp(data[r], data[j])
                j = r
            end
            if j == i
                break
            end
            data[i], data[j] = data[j], data[i]
            i = j
        end
    end
    for i in reverse(1:div(length(data), 2))
        _sift_down!(i)
    end
    return heap
end

function heap(data::Vector{T}; comparator::Function)::Heap{T} where T <: Real
    h = Heap(data; comparator=comparator)
    heapify!(h)
end

function heapSort!(heap::Heap{T})::Heap{T} where T <: Real
    data = heap.data
    cmp = heap.comparator
    n = length(data)
    heapify!(heap)
    for i in n:-1:2
        data[1], data[i] = data[i], data[1]
        _sift_down!(data, 1, i - 1, cmp)
    end
    return heap
end

function heapSort!(data::Vector{T}; comparator::Function)::Vector{T} where T <: Real
    heap_obj = heap(data; comparator=comparator)
    heapSort!(heap_obj)
    return heap_obj.data
end

function _sift_down!(data::Vector{T}, i::Int, n::Int, cmp::Function) where T
    while 2 * i <= n
        l = 2 * i
        r = 2 * i + 1
        j = i
        if l <= n && cmp(data[l], data[j])
            j = l
        end
        if r <= n && cmp(data[r], data[j])
            j = r
        end
        if j == i
            break
        end
        data[i], data[j] = data[j], data[i]
        i = j
    end
end

function maximum(heap::Heap{T})::Union{T, Nothing} where T <: Real
    isempty(heap.data) ? nothing : heap.data[1]
end
