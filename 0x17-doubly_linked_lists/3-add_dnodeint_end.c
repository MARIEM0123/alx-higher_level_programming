#include "lists.h"
/**
 * add_dnodeint_end - adds a node at the end
 * of a list
 * @head: the parameter
 * @n: parameter
 * Return: != NULL
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *h;
	dlistint_t *nw;

	nw = malloc(sizeof(dlistint_t));
	if (nw == NULL)
		return (NULL);

	nw->n = n;
	nw->next = NULL;

	h = *head;

	if (h != NULL)
	{
		while (h->next != NULL)
			h = h->next;
		h->next = nw;
	}
	else
	{
		*head = nw;
	}

	nw->prev = h;

	return (nw);
}
