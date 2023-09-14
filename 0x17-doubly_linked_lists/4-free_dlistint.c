#include "lists.h"
/**
 * free_dlistint - frees the list
 * @head: the parameter
 * Return: there is no return
 **/
void free_dlistint(dlistint_t *head)
{
	if (head == NULL)
	return;

	while (head->next)
	{
	head = head->next;
	free(head->prev);
	}
	free(head);
}
