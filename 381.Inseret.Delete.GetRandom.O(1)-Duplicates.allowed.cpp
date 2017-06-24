class RandomizedCollection {
public:
	/** Initialize your data structure here. */
	RandomizedCollection() : generator(time(0)), distribution(0, 0x7fffffff) {
		size = getExpandSize();
		data = new int[size];
		has = new char[size];
		used = 0;
		for (int i = 0; i<size; ++i)has[i] = 0;
	}

	/** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
	bool insert(int val) {
		if (size * 0.7 < used + 1) expand();
		bool ret = true;
		bool inserted = false;
		for (unsigned h = hash(val); ; h = (h + 1) % size)
		{
			if (has[h] <= 1)
			{
				int oldh = has[h];
				if (!inserted) {
					has[h] = 2;
					used++;
					data[h] = val;
					inserted = true;
				}
				if (oldh == 0)
				{
					break;
				}
			}
			else //(has[h] == 2)
			{
				if (data[h] == val)
				{
					ret = false;
				}
			}

		}
		return ret;
	}

	/** Removes a value from the collection. Returns true if the collection contained the specified element. */
	bool remove(int val) {
		for (unsigned h = hash(val); ; h = (h + 1) % size)
		{
			if (has[h] == 2)
			{
				if (data[h] == val) {
					has[h] = 1;
					//used --;
					return true;
				}
			}
			else if (has[h] == 0)
			{
				return false;
			}
		}
		return false;
	}

	/** Get a random element from the collection. */
	int getRandom() {
		while (1)
		{
			unsigned h = (unsigned)distribution(generator) % size;
			while (has[h] != 2)
			{
				h = (unsigned)distribution(generator) % size;
			}
			return data[h];
		}
		return 0;
	}


protected:
	unsigned getExpandSize(unsigned curSize = 0)
	{
		static vector<unsigned> primes = { 11, 23, 53, 97, 193, 389, 769,
			1543, 3079, 6151, 12289, 24593,
			49157, 98317, 196613, 393241, 786433,
			1572869, 3145739, 6291469, 12582917, 25165843,
			50331653, 100663319, 201326611 };
		auto it = upper_bound(primes.begin(), primes.end(), curSize);
		if (it == primes.end()) return *(it - 1);
		else return *it;
	}

	unsigned hash(int val)
	{
		return val%size;
	}

	void expand()
	{
		used = 0;
		unsigned newsize = getExpandSize(size);
		int *newdata = new int[newsize];
		char *newhas = new char[newsize];
		for (int i = 0; i<newsize; ++i)newhas[i] = 0;
		for (unsigned i = 0; i < size; ++i)
		{
			if (has[i] == 2)
			{
				used++;
				for (unsigned h = (unsigned)data[i] % newsize; ; h = (h + 1) % newsize)
				{
					if (newhas[h] <= 1)
					{
						newhas[h] = 2;
						newdata[h] = data[i];
						break;
					}
				}
			}
		}

		swap(size, newsize);
		swap(data, newdata);
		swap(has, newhas);

		delete newdata;
		delete newhas;
	}


	int *data;
	unsigned size;
	unsigned used;
	char *has;

	default_random_engine generator;
	uniform_int_distribution<int> distribution;

};