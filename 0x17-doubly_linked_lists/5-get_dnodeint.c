#include "lists.h"

/**
 * get_dnodeint_at_index - return the index of the list.
 * @head: pointer parameter to the head
 * @index: index of the node to find
 * Return: != null or null depending to the case
 **/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int s;
	dlistint_t *a;

	s = 0;
	if (head == NULL)
	return (NULL);

	a = head;
	while (a)
	{
	if (index == s)
	return (a);
	s++;
	a = a->next;
	}
	return (NULL);
}
