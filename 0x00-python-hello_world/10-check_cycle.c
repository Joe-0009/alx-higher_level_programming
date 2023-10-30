#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *t = list;
    listint_t *h = list;

    while (h != NULL && h->next != NULL)
    {
        t = t->next;
        h = h->next->next;

        if (t == h)
        {
            return (1);
        }
    }

    return (0);
}

