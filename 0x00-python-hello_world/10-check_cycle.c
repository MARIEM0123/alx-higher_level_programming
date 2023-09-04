#include "lists.h"

/**
 * check_cycle - The function to check if a linked list is a cycle or not
 * @list: linked list to be checked
 * Return: depends on the case 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *ls = list;
	listint_t *lf = list;

	if (!list)
		return (0);

	while (ls && lf && lf->next)
	{
		ls = ls->next;
		lf = lf->next->next;
		if (ls == lf)
			return (1);
	}

	return (0);
}
