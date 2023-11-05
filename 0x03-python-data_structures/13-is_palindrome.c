#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the listint_t list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t  *last_node = *head;
	int length = 0, j = 0;
	int *array;

	while (last_node != NULL)
	{
		last_node = last_node->next;
		length++;
	}
	array = malloc(sizeof(int) * length);
	if (array == NULL)
		return (0);

	last_node = *head;

	while (last_node)
	{
		array[j++] = last_node->n;
		last_node = last_node->next;
	}

	for (j = 0; j < length / 2; j++)
	{
		if (array[j] != array[length - j - 1])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
