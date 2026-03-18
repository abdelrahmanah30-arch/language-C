/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kali <marvin@42.fr>                        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 02:59:00 by kali              #+#    #+#             */
/*   Updated: 2026/03/18 03:12:48 by kali             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	ft_len(char *s)
{
	int	i;

	i = 0;
	while (s[i] != '\0')
		i++;
	return (i);
}

char	*ft_strdup(char *src)
{
	int		len;
	int		i;
	char	*dest;

	len = ft_len(src);
	dest = malloc(sizeof(char) * (len + 1));
	if (!dest)
		return (NULL);
	i = 0;
	while (i < len)
	{
		dest[i] = src[i];
		i++;
	}
	return (dest);
}
/*
int main(void)
{
    printf("test one:\n");
    char src[] = "teste";
    char *dest = ft_strdup(src);
    
    printf("src: %s\n", src);
    printf("dest: %s\n", dest);

    char src2[] = "teste";
    char *dest2 = ft_strdup(src2);
    
    printf("\ntest two:\n");
    printf("src2: %s\n", src2);
    printf("dest2: %s\n", dest2);
} */
