#include "lists.h"

/**
 * insert_node - The function inserts a number into a sorted singly-linked list.
 * @head: A pointer parameter
 * @number: the parameter to insert
 * Return: NULL or the pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *h, *e;

	e = malloc(sizeof(listint_t));
	if (e == NULL)
		return (NULL);
	e->n = number;

	if (node == NULL || node->n >= number)
	{
		e->next = node;
		*h = e;
		return (e);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = e;

	return (e);
}
