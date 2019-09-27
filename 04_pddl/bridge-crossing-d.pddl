(define (domain bridge-crossing)

	(:types
		Side Locatable - Object
		Person Torch - Locatable
	)

	(:predicates
		(located ?l - Locatable ?s - Side)
	)

	(:functions
		(travelTime ?p - Person)
	)

	(:durative-action Travel1
		:parameters (
			?person - Person
			?torch - Torch
			?origin - Side
			?destination - Side
		)
		:duration (= ?duration (travelTime ?person))
		:condition (and
			(at start (located ?person ?origin))
			(at start (located ?torch ?origin))
		)
		:effect (and
			(at start (not (located ?person ?origin)))
			(at start (not (located ?torch ?origin)))
			(at end (located ?torch ?destination))
			(at end (located ?person ?destination))
		)
	)

	(:durative-action Travel2
		:parameters (
			?person1 - Person
			?person2 - Person
			?torch - Torch
			?origin - Side
			?destination - Side
		)
		:duration (= ?duration (travelTime ?person1))
		:condition (and
			(at start (> (travelTime ?person1) (travelTime ?person2)))
			(at start (located ?person1 ?origin))
			(at start (located ?person2 ?origin))
			(at start (located ?torch ?origin))
		)
		:effect (and
			(at start (not (located ?person1 ?origin)))
			(at start (not (located ?person2 ?origin)))
			(at start (not (located ?torch ?origin)))
			(at end (located ?person1 ?destination))
			(at end (located ?person2 ?destination))
			(at end (located ?torch ?destination))
		)
	)
)