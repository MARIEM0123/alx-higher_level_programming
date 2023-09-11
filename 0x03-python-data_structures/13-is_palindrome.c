/*
 * Project: 13-is_palindrome.c
 * Function: the function for shecking if a palindrome
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a list
 * @hd: A pointer to the start node
 * Return: A pointer to the reversed list
 */
listint_t *reverse_listint(listint_t **hd)
{
	listint_t *nd = *hd, *next, *v = NULL;

	while (nd)
	{
		next = nd->next;
		nd->next = v;
		v = nd;
		nd = next;
	}

	*hd = v;
	return (*hd);
}
/**
 * is_palindrome - Checks if a list is a palindrome.
 * @head: A pointer to the head.
 * Return: -0 or 1 depending on the case
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rvs, *x;
	size_t l = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		l++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (l / 2) - 1; i++)
		temp = temp->next;

	if ((l % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rvs = reverse_listint(&temp);
	x = rvs;

	temp = *head;
	while (rvs)
	{
		if (temp->n != rvs->n)
			return (0);
		temp = temp->next;
		rvs = rvs->next;
	}
	reverse_listint(&x);

	return (1);
}
