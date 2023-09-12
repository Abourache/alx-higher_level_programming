#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: the head address of the linked list
 *
 * Return: 1 if it's a palindrome, 0 else
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int tab[2048], a = 0, y = 0;

	if (*head)
	{
		while (cur)
		{
			tab[a] = cur->n;
			cur = cur->next;
			a++;
		}

		while (y < a / 2)
		{
			if (tab[y] == tab[a - y - 1])
				y++;
			else
				return (0);
		}
	}
	return (1);
}
