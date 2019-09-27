(define (problem cross-bridge-4p)
	(:domain bridge-crossing)

	(:objects
		alberto - Person
		beatriz - Person
		cecilia - Person
		damian - Person
		torch - Torch
		west - Side
		east - Side
	)

	(:init
		(located alberto west)
		(located beatriz west)
		(located cecilia west)
		(located damian west)
		(located torch west)
		(= (travelTime alberto) 1) 
		(= (travelTime beatriz) 2) 
		(= (travelTime cecilia) 5) 
		(= (travelTime damian) 10) 
	)

	(:goal
		(and
			(located alberto east)
			(located beatriz east)
			(located cecilia east)
			(located damian east)
			(located torch east)
		)
	)

	(:metric minimize (total-time))
)