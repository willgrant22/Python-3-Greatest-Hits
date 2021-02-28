#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from scipy import sparse

original_matrix = np.array([[1, 0, 3], [0, 0, 6], [7, 0, 0]])
sparse_matrix = sparse.csr_matrix(original_matrix)
print(sparse_matrix)