/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_union.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kali <marvin@42.fr>                        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 04:14:32 by kali              #+#    #+#             */
/*   Updated: 2026/03/18 06:58:23 by kali             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	seen_before(char *s, int max, char c)
{
	int	i;

	i = 0;
	while (i < max)
	{
		if (s[i] == c)
			return (1);
		i++;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	int	i;
	int	j;

	if (argc == 3)
	{
		i = -1;
		while (argv[1][++i])
			if (!seen_before(argv[1], i, argv[1][i]))
				write (1, &argv[1][i], 1);
		j = -1;
		while (argv[2][++j])
			if (!seen_before(argv[1], i, argv[2][j]) &&
				!seen_before(argv[2], j, argv[2][j]))
				write (1, &argv[2][j], 1);
	}
	write (1, "\n", 2);
}
