/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the head address of the linked list
 * Return: 1 if it's a palindrome, 0 else
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int tab[2048], x = 0, y = 0;

	if (*head)
	{
		while (cur)
		{
			tab[x] = cur->n;
			cur = cur->next;
			x++;
		}

		while (y < x / 2)
		{
			if (tab[y] == tab[x - y - 1])
				y++;
			else
				return (0);
		}
	}
	return (1);
}
