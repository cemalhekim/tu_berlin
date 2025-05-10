function check_controllability(A, b)
    % CHECK_CONTROLLABILITY: Check if the system (A, b) is controllable.
    %
    % Inputs:
    %   A - State matrix (n x n)
    %   b - Input matrix (n x 1)
    %
    % Example usage:
    %   A = [1, 2; 0, -1];
    %   b = [0; 1];
    %   check_controllability(A, b);

    % Get the size of the state matrix A
    n = size(A, 1);
    
    % Initialize the controllability matrix
    ControllabilityMatrix = [];
    
    % Build the controllability matrix
    for i = 0:n-1
        ControllabilityMatrix = [ControllabilityMatrix, A^i * b];
    end
    
    % Calculate the rank of the controllability matrix
    rank_C = rank(ControllabilityMatrix);
    
    % Check controllability
    if rank_C == n
        fprintf('The system is controllable (rank = %d).\n', rank_C);
    else
        fprintf('The system is NOT controllable (rank = %d).\n', rank_C);
    end
end
