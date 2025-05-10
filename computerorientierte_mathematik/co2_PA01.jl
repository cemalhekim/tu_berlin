#  einen (”nicht-mutable”) Typ Pfad
struct Pfad
    source::Real
    target::Union{Real, Pfad}
end

# Method 1
pfad(source::Real, target::Real) = Pfad(source, target)
# Method 2
pfad(source::Real, target::Pfad) = Pfad(source, target)
# Method 3
pfad(source::Real) = Pfad(source, source)

# Infix-Operator und show Methode
# Infix-Operator fur Method 1
function ⇒(source::Real, target::Real)
    pfad(source, target)
end
# Infix-Operator fur Method 2
function ⇒(source::Real, target::Pfad)
    pfad(source, target)
end
# Infix-Operator fur Method 3
function ⇒(source::Real)
    pfad(source)
end

function Base.show(io::IO, p::Pfad)
    # Printing wie 4 ⇒ 5 ⇒ 6
    if p.target isa Pfad
        # Recursive teil
        print(io, "$(p.source) ⇒ ", p.target)
    else
        # Non-Pfand case
        print(io, "$(p.source) ⇒ $(p.target)")
    end
end

#  Konkatination von Pfaden
function *(f::Pfad, g::Pfad)

    # Verkettung von Pfaden
    if f.target isa Pfad
        # Recursive teil
        return Pfad(f.source, f.target * g)  
    else
        #Sicherstellen, dass die letzte Zahl von f und die erste Zahl von g übereinstimmen
        @assert f.target == g.source "assertion error" 
        # Non-Pfand case
        return Pfad(f.source, g)  
    end

end