#include "lists.h"

/**
 * dlistint_len - prints the number of elements
 * in a list
 * @h: head of the list
 * Return: =! NULL
 */
size_t dlistint_len(const dlistint_t *h)
{
	int i;

	i = 0;
	if (h == NULL)
		return (i);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		i++;
		h = h->next;
	}

	return (i);
}
