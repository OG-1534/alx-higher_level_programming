#include "lists.h"

/**
 * check_cycle - function in C that checks
 * if a singly linked list has a cycle in it
 * @list: linked list to check
 * Return: 0 no cycle 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slw, *fst;

	if (!list || !list->next)
		return (0);
	fst = list;
	slw = list;

	while (slw != NULL && fst != NULL && fst->next != NULL)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
		{
			return (1);
		}
	}
	return (0);
}
